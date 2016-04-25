'use strict';

var env = require('jsdom').env;
var fs = require('fs');

var html;
fs.readFile('html/368722.html', 'utf8', function(err, data) {
  if (err) {
    return console.log(err);
  }
  html = data;
  cont();
});

var cont = function() {
  env(html, function(errors, window) {

    if (errors) {
      console.log(errors);
    }
    var $ = require('jquery')(window);

    console.log("TPs ->");
    $('table.horario td.TP').each(function(index) {
      console.log(index + ": " + $(this).find('b a').first().text());
      console.log("turma: " + $(this).find('span.textopequenoc').text());
      console.log("horas: " + $(this).parent().find('td.k').text());
      console.log("dia: " + $(this).index());
      console.log("duracao: " + $(this).attr('rowspan'));
      console.log("profsig: " + $(this).find('table tr td.textod').text());
      console.log("prof: " + $(this).find('table tr td.textod acronym').attr('title'));

    });

    console.log("TEs ->");
    $('table.horario td.TE').each(function(index) {
      console.log(index + ": " + $(this).find('b a').first().text());
    });
    console.log("xTPs ->");
    $('table.dados tr.d').each(function(index) {
      console.log(index + ": " + $(this).find('td:first a').first().text());
    });




  });
}
