document.addEventListener('DOMContentLoaded', () => {
	document.querySelector('#expandbutton').onclick = closeNav;
	document.querySelector('#add').onclick = addChannel;

	var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
	socket.on('connect', () => {
		document.querySelector('#message').onSubmit = () => {
			const message = document.querySelector('#mes').value;
			socket.emit('submit message', {'message': message})
		};
	});

	socket.on('announce message', data => {
		const div = document.createElement('div');
        div.innerHTML = `${data.displayname}: ${data.selection}`;
        document.querySelector('#messages').append(div);
    });
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

function addChannel() {
	document.querySelector('#newChannel').style.display = 'initial';
}