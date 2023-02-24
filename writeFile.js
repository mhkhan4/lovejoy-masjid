const fs = require('fs');
const csv = require('csv-parser');
const createCsvWriter = require('csv-writer').createObjectCsvWriter;

const results = [];

fs.createReadStream('./FullYearTiming_LovejoyMasjid.csv')
  .pipe(csv())
  .on('data', (data) => {
    results.push(data);
  })
  .on('end', () => {
    for(let i = 0; i < results.length; i++){
        const newString = results[i]["Info"].replace(/,/g, "   ");
        results[i]["Info"] = newString;
    }

    // Write the updated CSV file
    const csvWriter = createCsvWriter({
        path: 'fixed.csv',
        header: [
          { id: 'Month', title: 'Month' },
          { id: 'Day', title: 'Day' },
          { id: 'Fajr Adhan', title: 'Fajr Adhan' },
          { id: 'Shouruq', title: 'Shouruq' },
          { id: 'Dhuhr Adhan', title: 'Dhuhr Adhan' },
          { id: 'Asr Adhan', title: 'Asr Adhan' },
          { id: 'Maghrib Adhan', title: 'Maghrib Adhan' },
          { id: 'Isha Adhan', title: 'Isha Adhan' },
          { id: '', title: '' },
          { id: 'Fajr Iqamah', title: 'Fajr Iqamah' },
          { id: 'Dhuhr Iqamah', title: 'Dhuhr Iqamah' },
          { id: 'Asr Iqamah', title: 'Asr Iqamah' },
          { id: 'Maghrib Iqamah', title: 'Maghrib Iqamah' },
          { id: 'Isha Iqamah', title: 'Isha Iqamah' },
          { id: 'Info', title: 'Info' },
        ],
      });
      csvWriter.writeRecords(results).then(() => {
        console.log('CSV file updated successfully');
      });
    });

