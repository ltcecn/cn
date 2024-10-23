/ server.js
const net = require('net');

const server = net.createServer((socket) => {
    

    socket.on('data', (data) => {
        const numbers = data.toString().split('\n').map(Number);
        const sum = numbers[0] + numbers[1];
        socket.write(`The sum is: ${sum}\n`);
        socket.end(); // Close the connection after sending the result
    });
});

server.listen(5000, () => {
    console.log('Server is waiting for a connection on port 5000...');
});