document$.subscribe(function () {
  // Only activate on pages that opt in with: <div class="table-filter"></div>
  // Each container filters the first data table that follows it, so a page
  // may have several.
  document.querySelectorAll("div.table-filter").forEach(function (container) {
    // Find the next data table after the container (it may be wrapped in
    // scroll-wrapper divs), stopping if we reach another filter container.
    var table = null;
    for (var el = container.nextElementSibling; el; el = el.nextElementSibling) {
      if (el.matches("div.table-filter")) break;
      table = el.matches("table:not([class])") ? el : el.querySelector("table:not([class])");
      if (table) break;
    }
    if (!table) return;

    // Place the filter input inside the opt-in div
    var input = document.createElement("input");
    input.type = "text";
    input.placeholder = "Type to filter rows…";
    input.className = "table-filter-input";
    container.appendChild(input);

    // Help text shown when the query is being interpreted as a regex
    var help = document.createElement("div");
    help.className = "table-filter-help";
    help.hidden = true;
    container.appendChild(help);

    input.addEventListener("input", function () {
      // A query starting with "/" (ignoring leading whitespace) is a regex,
      // optionally closed with "/flags", e.g. "/cs 1\d\d" or "/smith/i".
      // Matching is case-insensitive unless flags are given explicitly.
      var raw = this.value.replace(/^\s+/, "");
      var term = this.value.toLowerCase();
      var regex = null;
      if (raw.charAt(0) === "/") {
        var body = raw.slice(1);
        var flags = "i";
        var m = body.match(/^(.*)\/([a-z]*)$/);
        if (m) { body = m[1]; flags = m[2]; }
        try {
          regex = new RegExp(body, flags.replace(/[gy]/g, ""));
          help.textContent = "Interpreting query as a regular expression: " + regex;
          help.classList.remove("table-filter-error");
        } catch (e) {
          help.textContent = "Invalid regular expression: " + e.message;
          help.classList.add("table-filter-error");
          regex = /(?:)/;  // show all rows while the regex is incomplete
        }
        help.hidden = false;
      } else {
        help.hidden = true;
      }
      var rows = table.querySelectorAll("tbody tr");

      // Collect the full text for each row group (accounting for rowspans).
      // A row with a rowspan cell "owns" the subsequent spanned rows, so
      // we test the combined text of the entire group.
      var groups = [];  // [{startRow, rows: [tr, ...], text: ""}]
      rows.forEach(function (row) {
        // A row starts a new group if any of its cells have rowspan > 1,
        // or if it is not already part of an existing group.
        var startsGroup = false;
        row.querySelectorAll("td").forEach(function (td) {
          if (td.rowSpan > 1) startsGroup = true;
        });
        if (startsGroup || groups.length === 0 ||
            groups[groups.length - 1].rows.length >=
            groups[groups.length - 1].span) {
          var maxSpan = 1;
          row.querySelectorAll("td").forEach(function (td) {
            if (td.rowSpan > maxSpan) maxSpan = td.rowSpan;
          });
          groups.push({ rows: [row], span: maxSpan, text: row.textContent });
        } else {
          var g = groups[groups.length - 1];
          g.rows.push(row);
          g.text += " " + row.textContent;
        }
      });

      groups.forEach(function (g) {
        var match = regex ? regex.test(g.text)
                          : g.text.toLowerCase().includes(term);
        var visible = match ? "" : "none";
        g.rows.forEach(function (row) { row.style.display = visible; });
      });
    });
  });
});
