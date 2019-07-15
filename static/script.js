document.addEventListener('DOMContentLoaded', () => {
	document.querySelector('#expandbutton').onclick = openNav;
	});



function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
  document.querySelector('#expandbutton').onclick = closeNav;
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginLeft= "0";
  document.querySelector('#expandbutton').onclick = openNav;
}