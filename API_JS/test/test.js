var request = require('request');
const expect = require("chai").expect;

var options = {
  'method': 'GET',
  'url': 'https://api.deezer.com/search?q=artist:"slipknot"',
  'headers': {
    'Cookie': 'dzr_uniq_id=dzr_uniq_id_fr066ce0c22f0e4d04a783bca3ea03a6a160065a'
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
});


describe('Consultar el estado GET', function() {
    it('Validar codigo de respuesta', function(done) {
        request.get({ url: options.url },
            function(error, response, body) {
                    const bodyObj = JSON.parse(body);
                    expect(response.statusCode).to.be.oneOf([200,201,201]);
                    console.log(response.statusCode)
                done();
            });
    });
});

describe('Consultar el estado GET', function() {
    it('Verificar el nombre del artista', function(done) {
        request.get({ url: options.url },
            function(error, response, body) {
                    const bodyObj = JSON.parse(body);
                    expect(bodyObj.data[0].artist.name).to.equal("Slipknot");
                    console.log(bodyObj.data[0].artist.name)
                done();
            });
    });
});
