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





// client.js
const net = require('net');
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const client = net.createConnection({ port: 5000, host:  '192.168.1.12' }, () => {
    console.log('Connected to server!');
    rl.question('Enter first number: ', (num1) => {
        rl.question('Enter second number: ', (num2) => {
            client.write(`${num1}\n${num2}\n`); // Send both numbers
        });
    });
});

client.on('data', (data) => {
    console.log(data.toString());
    client.end(); // Close the connection after receiving the result
});