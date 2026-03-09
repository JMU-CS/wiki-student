document$.subscribe(function () {
  // Only activate on pages that opt in with: <div id="table-filter"></div>
  var container = document.getElementById("table-filter");
  if (!container) return;

  // Find the first data table after the container
  var table = container.parentNode.querySelector("table:not([class])");
  if (!table) return;

  // Place the filter input inside the opt-in div
  var input = document.createElement("input");
  input.type = "text";
  input.placeholder = "Type to filter rows\u2026";
  input.className = "table-filter";
  container.appendChild(input);

  input.addEventListener("input", function () {
    var term = this.value.toLowerCase();
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
          groups.push({ rows: [row], span: maxSpan, text: row.textContent.toLowerCase() });
        } else {
          var g = groups[groups.length - 1];
          g.rows.push(row);
          g.text += " " + row.textContent.toLowerCase();
        }
      });

      groups.forEach(function (g) {
        var visible = g.text.includes(term) ? "" : "none";
        g.rows.forEach(function (row) { row.style.display = visible; });
      });
    });
});
