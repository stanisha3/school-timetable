import React, { useState, useEffect } from 'react';
import TeacherForm from '../components/TeacherForm';
import TeacherList from '../components/TeacherList';
import axios from 'axios';

const Teachers = () => {
  const [teachers, setTeachers] = useState([]);

  const fetchTeachers = async () => {
    try {
      const response = await axios.get('http://localhost:8000/teachers');
      setTeachers(response.data);
    } catch (error) {
      console.error('Error fetching teachers:', error);
    }
  };

  const addTeacher = async (newTeacher) => {
    try {
      const teacherData = {
        name: newTeacher,
        email: null,  // Optional field
        hashed_password: null  // Optional field
      };
      const response = await axios.post('http://localhost:8000/teachers', teacherData);
      setTeachers([...teachers, response.data]);
    } catch (error) {
      console.error('Error adding teacher:', error);
    }
  };

  const deleteTeacher = async (id) => {
    try {
      await axios.delete(`http://localhost:8000/teachers/${id}`);
      setTeachers(teachers.filter((t) => t.id !== id));
    } catch (error) {
      console.error('Error deleting teacher:', error);
    }
  };

  useEffect(() => {
    fetchTeachers();
  }, []);

  return (
    <div className="max-w-3xl mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4 text-center">Teacher Management</h1>
      <TeacherForm onAdd={addTeacher} />
      <TeacherList teachers={teachers} deleteTeacher={deleteTeacher} />
    </div>
  );
};

export default Teachers;
