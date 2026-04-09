class AppController {
  static getHomepage(req, res) {
    res.type('text/plain');
    res.status(200).send('Hello Holberton School!');
  }
}

export default AppController;
