// SEARCH
document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.getElementById("searchInput");
    searchInput.addEventListener("keyup", function() {
        const filter = searchInput.value.toLowerCase();
        const table = document.getElementById("customers");
        const tr = table.getElementsByTagName("tr");

        // Loop through all table rows, except the first one (headers)
        for (let i = 1; i < tr.length; i++) {
            const tdArray = tr[i].getElementsByTagName("td");
            let found = false;
            
            // Loop through all table cells in the row
            for (let j = 0; j < tdArray.length; j++) {
                const td = tdArray[j];
                if (td) {
                    const txtValue = td.textContent || td.innerText;
                    if (txtValue.toLowerCase().indexOf(filter) > -1) {
                        found = true;
                        break;
                    }
                }
            }

            // If a match is found, show the row, otherwise hide it
            tr[i].style.display = found ? "" : "none";
        }
    });
});

// DATA EXPIRATION
// document.addEventListener("DOMContentLoaded", function() {
//     const dateCells = document.querySelectorAll(".date-cell");
    
//     const monthNames = {
//         'Janeiro': 0,
//         'Fevereiro': 1,
//         'Março': 2,
//         'Abril': 3,
//         'Maio': 4,
//         'Junho': 5,
//         'Julho': 6,
//         'Agosto': 7,
//         'Setembro': 8,
//         'Outubro': 9,
//         'Novembro': 10,
//         'Dezembro': 11
//     };

//     dateCells.forEach(cell => {
//         const dateText = cell.textContent.trim();
//         const dateParts = dateText.split(' ');

//         const day = parseInt(dateParts[0]);
//         const month = monthNames[dateParts[2]];
//         const year = parseInt(dateParts[4]);
//         const time = dateParts[6].split(':');
//         const hours = parseInt(time[0]);
//         const minutes = parseInt(time[1]);

//         const cellDate = new Date(year, month, day, hours, minutes);
//         const currentDate = new Date();

//         if (cellDate < currentDate) {
//             const badge = document.createElement("span");
//             badge.textContent = "data expirada";
//             badge.classList.add("expired-badge");
//             cell.appendChild(badge);
//         }
//     });
// });