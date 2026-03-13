document$.subscribe(function () {
  // Merge table cells that contain only ":::" (DokuWiki rowspan convention).
  // A ":::" cell means "merge with the cell above in this column."
  document.querySelectorAll(".md-typeset table:not([class])").forEach(function (table) {
    var rows = Array.from(table.querySelectorAll("tr"));
    if (rows.length < 2) return;

    // Build a 2D grid that maps visual (row, col) to the actual <td>/<th>.
    // This correctly handles cells that already have rowspan/colspan.
    var grid = [];
    rows.forEach(function (row, r) {
      if (!grid[r]) grid[r] = [];
      var cells = row.querySelectorAll("td, th");
      var c = 0;
      Array.from(cells).forEach(function (cell) {
        while (grid[r][c]) c++;                // skip occupied slots
        var rs = cell.rowSpan || 1;
        var cs = cell.colSpan || 1;
        for (var dr = 0; dr < rs; dr++) {
          for (var dc = 0; dc < cs; dc++) {
            if (!grid[r + dr]) grid[r + dr] = [];
            grid[r + dr][c + dc] = { cell: cell, origin: dr === 0 && dc === 0 };
          }
        }
        c += cs;
      });
    });

    // Determine the number of visual columns
    var numCols = 0;
    grid.forEach(function (row) { if (row.length > numCols) numCols = row.length; });

    // For each visual column, walk downward and merge ":::" cells upward.
    for (var col = 0; col < numCols; col++) {
      var anchor = null;
      for (var r = 0; r < grid.length; r++) {
        var entry = grid[r] && grid[r][col];
        if (!entry || !entry.origin) continue;
        var cell = entry.cell;
        if (cell.textContent.trim() === ":::") {
          if (anchor) {
            anchor.rowSpan = (anchor.rowSpan || 1) + (cell.rowSpan || 1);
            cell.remove();
          }
        } else {
          anchor = cell;
        }
      }
    }

    // Remove any rows that are now completely empty (all cells were merged)
    rows.forEach(function (row) {
      if (row.querySelectorAll("td, th").length === 0) row.remove();
    });
  });
});
