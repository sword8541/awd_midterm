// Import libraries
const fs = require("fs");
const express = require("express");
const bodyParser = require("body-parser");
const mysql = require("mysql2");
const mustacheExpress = require("mustache-express");

// Initialise objects and declare constants
const app = express();
const port = 8000;

const db = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "1234",
  database: "car_renting_info",
});
//set up the default page
const defaultPage = fs.readFileSync(
  `${__dirname}/templates/default.html`,
  "utf-8"
);

db.connect((err) => {
  if (err) {
    throw err;
  }
  console.log("Connected to database");
});

app.engine("html", mustacheExpress());
app.set("view engine", "html");
app.set("views", "./templates");
app.use(bodyParser.urlencoded({ extended: true }));

function templateRenderer(template, response) {
  return function (error, results, fields) {
    if (error) {
      throw error;
    }
    response.render(template, { data: results });
  };
}

app.get("/", function (req, res) {
  res.writeHead(200, { "Content-type": "text/html" });
  res.end(defaultPage);
});

app.get("/car_counts", function (req, res) {
  const data = {};
  db.query(
    "select count(*) as car_counts ,fuel_type from cars GROUP BY fuel_type  ORDER BY car_counts DESC",
    templateRenderer("car_counts", res)
  );
});

app.get("/states", function (req, res) {
  const data = {};
  db.query(
    "select count(*) as car_counts,state from cars INNER JOIN cities ON cars.city_id = cities.city_id    INNER JOIN states  ON cities.state_id = states.state_id    GROUP BY states.state    ORDER BY car_counts DESC     LIMIT 10",
    templateRenderer("states", res)
  );
});
app.listen(
  port,
  () => console.log(`listening on port ${port}`) // success callback
);
