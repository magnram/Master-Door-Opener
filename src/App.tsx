import React, { useState } from 'react';
import { Redirect } from "react-router-dom";
import './App.css';

function App() {
  const [disabled, setDisabled] = useState(false);
  window.location.href = "http://192.168.0.12:3000"
  return (
    <div>
    Test
    </div> 
  );
}

export default App;
