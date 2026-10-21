document$.subscribe(function () {
  // Split each auto-index list of events into "Upcoming" and "Past" using the
  // data-start / data-end attributes written by partials/auto-index.html.
  // This runs in the browser because the static build can't know "today".

  // Parse "YYYY-MM-DD", "YYYY-MM-DD HH:MM", or "YYYY-MM-DDTHH:MM:SS" as
  // local time. Returns null if the value isn't recognizable.
  function parse(value) {
    var m = /^(\d{4})-(\d{2})-(\d{2})(?:[T ](\d{2}):(\d{2}))?/.exec(value || "");
    if (!m) return null;
    return {
      date: new Date(+m[1], m[2] - 1, +m[3], +(m[4] || 0), +(m[5] || 0)),
      allDay: !m[4],
    };
  }

  // Midnight at the end of the given day
  function endOfDay(date) {
    return new Date(date.getFullYear(), date.getMonth(), date.getDate() + 1);
  }

  // An event stays upcoming until its end time, or until the end of the day
  // when no end time is given.
  function endsAt(start, end) {
    if (end && !end.allDay && end.date > start.date) return end.date;
    return endOfDay((end || start).date);
  }

  // Number of calendar days from today until the given date
  function daysFrom(today, date) {
    var day = new Date(date.getFullYear(), date.getMonth(), date.getDate());
    return Math.round((day - today) / 86400000);
  }

  // Highlight events later this week (but after tomorrow) with a pill,
  // e.g., "This Friday"
  function badge(item, start, today) {
    var days = daysFrom(today, start);
    if (days < 2 || days > 6) return;
    var pill = document.createElement("span");
    pill.className = "auto-index__badge";
    pill.textContent = "This " + start.toLocaleDateString("en-US", { weekday: "long" });
    item.appendChild(pill);
  }

  var now = new Date();
  var today = new Date(now.getFullYear(), now.getMonth(), now.getDate());

  document.querySelectorAll("ul.auto-index__list").forEach(function (list) {
    var upcoming = [];
    list.querySelectorAll(":scope > li").forEach(function (item) {
      var start = parse(item.dataset.start);
      if (!start) return;
      if (now < endsAt(start, parse(item.dataset.end))) {
        upcoming.push({ item: item, start: start.date });
        badge(item, start.date, today);
      }
    });

    // Lists with nothing upcoming (e.g., past semesters) stay as they are
    if (upcoming.length === 0) return;

    var tag = list.dataset.heading || "h2";
    function heading(text) {
      var h = document.createElement(tag);
      h.textContent = text;
      return h;
    }

    // Soonest first, so the next event is at the top
    upcoming.sort(function (a, b) { return a.start - b.start; });
    var next = document.createElement("ul");
    next.className = "auto-index__list";
    upcoming.forEach(function (u) { next.appendChild(u.item); });

    list.before(heading("Upcoming"), next);
    // The original list keeps the past events, newest first
    if (list.children.length > 0) list.before(heading("Past"));
  });
});
