import React, { useState } from 'react';
import './App.css';

function App() {
  const [disabled, setDisabled] = useState(false);
  return (
    <div className="App">
      <header className="App-header">
        <button 
          style={{width: 200, height: 150, fontSize: 40, borderRadius: 0}}
          disabled={disabled}
          onClick={() => {
            setDisabled(true)
            fetch('http://10.53.40.133:8090')
            .catch(() => setDisabled(false))   
          }
          }
        >
          Open
        </button>
      </header>
    </div>
  );
}

export default App;
