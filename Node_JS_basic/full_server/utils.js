import fs from 'fs';

const readDatabase = (filePath) => new Promise((resolve, reject) => {
  fs.readFile(filePath, 'utf8', (error, data) => {
    if (error) {
      reject(new Error('Cannot load the database'));
      return;
    }

    const lines = data
      .split('\n')
      .map((line) => line.trim())
      .filter((line) => line !== '');

    const students = lines.slice(1);
    const studentsByField = {};

    students.forEach((student) => {
      const [firstname, , , field] = student.split(',');

      if (!studentsByField[field]) {
        studentsByField[field] = [];
      }

      studentsByField[field].push(firstname);
    });

    resolve(studentsByField);
  });
});

export default readDatabase;
