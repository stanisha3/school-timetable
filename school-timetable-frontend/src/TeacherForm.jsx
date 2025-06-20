import { useState } from 'react';

const TeacherForm = ({ onAdd }) => {
  const [name, setName] = useState('');

  const handleSubmit = e => {
    e.preventDefault();
    if (name.trim()) {
      onAdd(name);
      setName('');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="mb-4 flex gap-2">
      <input
        type="text"
        placeholder="Enter teacher name"
        value={name}
        onChange={e => setName(e.target.value)}
        className="border px-3 py-2 rounded w-full"
      />
      <button type="submit" className="bg-blue-500 text-white px-4 rounded hover:bg-blue-600">Add</button>
    </form>
  );
};

export default TeacherForm;
