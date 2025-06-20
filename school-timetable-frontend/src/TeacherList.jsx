const TeacherList = ({ teachers, onDelete }) => {
  return (
    <ul className="divide-y">
      {teachers.map(teacher => (
        <li key={teacher.id} className="flex justify-between py-2">
          <span>{teacher.name}</span>
          <button
            onClick={() => onDelete(teacher.id)}
            className="text-red-500 hover:text-red-700"
          >
            Delete
          </button>
        </li>
      ))}
    </ul>
  );
};

export default TeacherList;
