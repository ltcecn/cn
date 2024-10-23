function hammingCode(dataBits) {
    const len = dataBits.length;
    let parityCount = 0;

    // Calculate parity bits needed
    while (2 ** parityCount < len + parityCount + 1) parityCount++;

    const hamming = Array(len + parityCount).fill('0');

    // Insert data bits and mark parity positions
    let dataIndex = 0;
    for (let i = 0; i < hamming.length; i++) {
        if (i + 1 === 2 ** Math.floor(Math.log2(i + 1))) {
            hamming[i] = 'p'; // Placeholder for parity
        } else {
            hamming[i] = dataBits[dataIndex++];
        }
    }

    // Calculate parity bits
    for (let i = 0; i < parityCount; i++) {
        const pos = 2 ** i;
        let count = 0;
        for (let j = pos - 1; j < hamming.length; j += pos * 2) {
            const segment = hamming.slice(j, j + pos);
            count += [...segment].filter(b => b === '1').length; // Convert to array to filter
        }
        hamming[pos - 1] = count % 2 ? '1' : '0';
    }

    return hamming.join('');
}

function detectAndCorrect(code) {
    let errorPos = 0;

    for (let i = 0; (1 << i) < code.length + 1; i++) {
        const pos = 2 ** i;
        let count = 0;
        for (let j = pos - 1; j < code.length; j += pos * 2) {
            const segment = code.slice(j, j + pos);
            count += [...segment].filter(b => b === '1').length; // Convert to array to filter
        }
        if (count % 2) errorPos += pos;
    }

    if (errorPos) {
        const corrected = code.split('');
        corrected[errorPos - 1] = corrected[errorPos - 1] === '0' ? '1' : '0';
        return { status: `Error at position ${errorPos}`, correctedCode: corrected.join('') };
    }
    return { status: "No error", correctedCode: code };
}

// Example usage
const dataBits = "1011";
const hamming = hammingCode(dataBits);
console.log("Hamming Code:", hamming);

const receivedCode = "0110110"; // Example received code
const result = detectAndCorrect(receivedCode);
console.log("Status:", result.status);
console.log("Corrected Code:", result.correctedCode);