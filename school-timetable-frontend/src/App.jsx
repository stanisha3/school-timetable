import React, { useState, useEffect } from 'react';
import Teachers from './pages/Teachers';
import Login from './pages/Login';

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      setIsLoggedIn(true);
    }
  }, []);

  const handleLogin = () => {
    setIsLoggedIn(true);
  };

  return (
    <div className="min-h-screen bg-gray-100 p-4">
      {isLoggedIn ? (
        <>
          <h1 className="text-3xl font-bold text-center mb-6">School Timetable</h1>
          <Teachers />
        </>
      ) : (
        <Login onLogin={handleLogin} />
      )}
    </div>
  );
}

export default App;
