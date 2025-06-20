import React, { useState } from 'react';
import axios from 'axios';

const Login = ({ onLogin }) => {
  const [isSignup, setIsSignup] = useState(false);
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);
    try {
      if (isSignup) {
        await axios.post('http://localhost:8000/users', {
          name,
          email,
          password
        });
        setIsSignup(false);
      } else {
        const params = new URLSearchParams();
        params.append('username', email);
        params.append('password', password);
        const response = await axios.post('http://localhost:8000/auth/token', params, {
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        });
        localStorage.setItem('token', response.data.access_token);
        if (onLogin) onLogin();
      }
    } catch (err) {
      if (err.response && err.response.data && err.response.data.detail) {
        setError(err.response.data.detail);
      } else {
        setError(isSignup ? 'Signup failed. Please try again.' : 'Invalid email or password');
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex items-center justify-center w-screen h-screen bg-gradient-to-br from-indigo-100 to-purple-100">
      <div className="bg-white p-8 sm:p-10 rounded-2xl shadow-xl w-full max-w-sm flex flex-col justify-center">
        <div className="flex justify-center mb-6">
          <div className="bg-indigo-100 p-3 rounded-full">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-8 w-8 text-indigo-600" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 2L1 21h22L12 2zm0 3.84L18.93 19H5.07L12 5.84zM11 10v6h2v-6h-2zm0 8v2h2v-2h-2z"/>
            </svg>
          </div>
        </div>

        <h2 className="text-2xl text-gray-800 font-bold text-center mb-6">
          {isSignup ? 'SIGN UP' : 'LOG IN'}
        </h2>

        {error && <p className="text-red-500 text-sm mb-4 text-center">{error}</p>}

        <form onSubmit={handleSubmit}>
          {isSignup && (
            <div className="mb-4">
              <label className="text-sm text-gray-600">Name</label>
              <div className="flex items-center border-b border-gray-300 py-1">
                <input
                  type="text"
                  value={name}
                  onChange={e => setName(e.target.value)}
                  className="bg-transparent outline-none w-full text-gray-700 placeholder-gray-400"
                  placeholder="Enter full name"
                  required
                />
              </div>
            </div>
          )}

          <div className="mb-4">
            <label className="text-sm text-gray-600">Email</label>
            <div className="flex items-center border-b border-gray-300 py-1">
              <input
                type="text"
                value={email}
                onChange={e => setEmail(e.target.value)}
                className="bg-transparent outline-none w-full text-gray-700 placeholder-gray-400"
                placeholder="Enter email"
                required
              />
            </div>
          </div>

          <div className="mb-4">
            <label className="text-sm text-gray-600">Password</label>
            <div className="flex items-center border-b border-gray-300 py-1">
              <input
                type="password"
                value={password}
                onChange={e => setPassword(e.target.value)}
                className="bg-transparent outline-none w-full text-gray-700 placeholder-gray-400"
                placeholder="Enter password"
                required
              />
            </div>
          </div>

          {!isSignup && (
            <div className="flex items-center mb-6">
              <input type="checkbox" className="mr-2" />
              <label className="text-gray-600 text-sm">Remember me</label>
            </div>
          )}

          <button
            type="submit"
            className="w-full bg-indigo-600 text-white font-semibold py-2 rounded-lg hover:bg-indigo-700 transition"
            disabled={loading}
          >
            {loading ? (isSignup ? 'Signing Up...' : 'Logging In...') : isSignup ? 'Sign Up' : 'Login'}
          </button>
        </form>

        <div className="text-center mt-4">
          {!isSignup && (
            <a href="#" className="text-indigo-600 text-sm hover:text-indigo-700">
              Forgot Password?
            </a>
          )}
        </div>

        <div className="text-center mt-4">
          <p className="text-sm text-gray-600">
            {isSignup ? 'Already have an account?' : "Don't have an account?"}{' '}
            <button
              onClick={() => setIsSignup(!isSignup)}
              className="text-indigo-600 hover:underline focus:outline-none"
            >
              {isSignup ? 'Log in' : 'Sign up'}
            </button>
          </p>
        </div>
      </div>
    </div>
  );
};

export default Login;
