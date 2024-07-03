// header scroll
// we will now write code to make sure the window is any of the sections and not the area between the sections
let nav = document.querySelector(".navbar");
window.onscroll = function() {
    if (document.documentElement.scrollTop > 20) {
        nav.classList.add("header-scrolled");
    } else {
        nav.classList.remove("header-scrolled");
    }
}

// nav hide in mobile view
let navBar = document.querySelectorAll(".nav-link");
let navCollapse = document.querySelector(".navbar-collapse.collapse");

navBar.forEach(function(a){
    a.addEventListener("click", function(){
        navCollapse.classList.remove("show");
    })
})

// menu_edit.js

// Function to handle click event on menu cards
function editMenu(day) {
    // Prompt the user to edit the menu
    var newMenu = prompt("Edit the menu for " + day + ":");

    // If the user entered a new menu
    if (newMenu !== null) {
        // Send an AJAX request to update the menu in the database
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                // Display a success message
                alert("Menu for " + day + " updated successfully!");
                // Reload the page to reflect the changes
                location.reload();
            }
        };
        xhttp.open("POST", "update_menu.php", true); // Change "update_menu.php" to the PHP file handling the database update
        xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhttp.send("day=" + day + "&menu=" + newMenu);
    }
}

  
