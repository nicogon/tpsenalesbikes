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

      //Esta poronga es si quiero filtrar por estaciones cerca de determinado punto (para ponele despues comparar palermo con el centro)

      latitude = -34.5910737; //-34.613457;
      longitude = -58.3799953; //-58.4401581;

      radius = 0.02;
      stations = stations.filter(station => {
        return (
          radius > Math.abs(station.address.longitude - longitude) &&
          radius > Math.abs(station.address.latitude - latitude)
        );
      });

      //corto ejecucion porque si no rompe despues
      if (stations.length == 0) throw "asd";

      // otros filtros para probar de una sola estacion
      //   station = stations.find(station => station["station_number"] == 256);

      count = 0;

      count2 = 0;
      stations.forEach(station => {
        count2 += station.status.total_disabled_bikes;
        count += station.status.total_available_bikes;
      });

      fs.appendFileSync(
        "junk.csv",
        //  `${timeStamp},${station.status.total_available_bikes}\n` aca si solo lo quiero hacer ocn una estacion
        `${timeStamp},${count},${count2}\n`
      );
      //     console.log(station)
    } catch (e) {
      console.log(e);
    }
  });
});
