const fs = require("fs");
var path = require("path");
var moment = require("moment");

var glob = require("glob");

// options is optional

glob("*.txt", function(er, files) {
  try {
    fs.unlinkSync("junk.csv");
    fs.appendFileSync("junk.csv", "date,bikes,broken\n");
  } catch (e) {}
  files.forEach(file => {
    const timeStamp = moment(file, "DDD-hh-mm").unix();

    try {
      let stations = JSON.parse(fs.readFileSync(file));


      arrNames = ['398 - Rojas','299 - HIDALGO', '241 - Sanatorio Mendez', '272 - Plaza Bruno Giordano'];

   
      latitude=-34.5910737;//-34.613457;
      longitude=-58.3799953//-58.4401581;

        radius = 0.020;
      stations =  stations.filter(station => {
       return   radius > Math.abs(station.address.longitude - longitude) && radius > Math.abs(station.address.latitude - latitude)
      })




        console.log(stations.length)
      if (stations.length == 0) throw "asd";

      //   station = stations.find(station => station["station_number"] == 256);

      count = 0;

      count2 = 0;
      stations.forEach(station => {
        count2 += station.status.total_disabled_bikes
        count += station.status.total_available_bikes;
      });

      fs.appendFileSync(
        "junk.csv",
        //  `${timeStamp},${station.status.total_available_bikes}\n`
        `${timeStamp},${count},${count2}\n`
      );
      //     console.log(station)
    } catch (e) {
      console.log(e);
    }
  });
});
