import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(req, res) {
    const database = process.argv[2];

    readDatabase(database)
      .then((studentsByField) => {
        const fields = Object.keys(studentsByField).sort((a, b) => a.localeCompare(b, undefined, { sensitivity: 'base' }));

        const responseLines = ['This is the list of our students'];
        fields.forEach((field) => {
          const firstnames = studentsByField[field];
          responseLines.push(`Number of students in ${field}: ${firstnames.length}. List: ${firstnames.join(', ')}`);
        });

        res.type('text/plain');
        res.status(200).send(responseLines.join('\n'));
      })
      .catch(() => {
        res.type('text/plain');
        res.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    const major = req.params.major;
    const database = process.argv[2];

    if (major !== 'CS' && major !== 'SWE') {
      res.type('text/plain');
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(database)
      .then((studentsByField) => {
        res.type('text/plain');
        res.status(200).send(`List: ${studentsByField[major].join(', ')}`);
      })
      .catch(() => {
        res.type('text/plain');
        res.status(500).send('Cannot load the database');
      });
  }
}

export default StudentsController;
