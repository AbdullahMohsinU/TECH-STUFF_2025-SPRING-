function appendValue(value) {
    document.getElementById('result').value += value;
    }
    function clearResult() {
    document.getElementById('result').value = '';
    }
    function calculateResult() {
    try {
    const result = eval(document.getElementById('result').value);
    document.getElementById('result').value = result;
    } catch {
    document.getElementById('result').value = 'Error';
    }
    }
    document.addEventListener('keydown', function(event) {
        const key = event.key;
        if (!isNaN(key) || ['+', '-', '*', '/', '.'].includes(key)) {
            appendValue(key);
        } else if (key === 'Enter') {
            calculateResult();
        } else if (key === 'Backspace') {
            const current = document.getElementById('result').value;
            document.getElementById('result').value = current.slice(0, -1);
        } else if (key === 'Escape') {
            clearResult();
        }
    });
    