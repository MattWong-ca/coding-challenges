// COUNTER APP - BFE.dev

import React from 'react'
import { useState } from 'react';

export function App() {

  const [counter, setCounter] = useState(0);

  return (
    <div>
      <button data-testid="decrement-button" onClick={() => setCounter(counter - 1)}>-</button>
      <button data-testid="increment-button" onClick={() => setCounter(counter + 1)}>+</button>
      <p>clicked: {counter}</p>
    </div>
  )
}
