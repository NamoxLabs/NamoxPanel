import '../scss/main.scss';
import $ from 'jquery';
import 'materialize-css/dist/js/materialize';
import 'jquery.cookie';

import React from 'react';
import ReactDOM from 'react-dom';
import Relay from 'react-relay';
import SVGInjector from 'svg-injector-2';

let csrftoken = $.cookie('csrftoken');

function csrfSafeMethod (method) {
  return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
}

$.ajaxSetup({
  beforeSend: function (xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader('X-CSRFToken', csrftoken);
    }
  }
});

Relay.injectNetworkLayer(
  new Relay.DefaultNetworkLayer('/graphql/', {
    credentials: 'same-origin',
    headers: {
      'X-CSRFToken': csrftoken
    }
  })
);

new SVGInjector().inject(document.querySelectorAll('svg[data-src]'));

let getAjaxError = (response) => {
  console.log('getAjaxError');
  console.log(response);
  let ajaxError = $.parseJSON(response.responseText).error.quantity;
  console.log('ajaxError');
  console.log(ajaxError);
  return ajaxError;
};

$(function() {
  $('.carousel.carousel-slider').carousel({fullWidth: true}); console.log('Carousel Slider ready!');
  $('.button-collapse').sideNav(); console.log('Button Collapse ready!');
  $('.parallax').parallax(); console.log('Parallax ready!');
  $('.carousel').carousel(); console.log('Normal Carousel ready!');
});

// jQuery Document Ready
$(document).ready(function() {
  console.log('Welcome');
});

// New address dropdown
let $addressShow = $('.address_show label');
let $addressHide = $('.address_hide label');
let $addressForm = $('.checkout__new-address');
let $initialValue = $('#address_new_address').prop('checked');
$addressShow.click((e) => {
  $addressForm.slideDown('slow');
});
$addressHide.click((e) => {
  $addressForm.slideUp('slow');
});
if ($initialValue) {
  $addressForm.slideDown(0);
} else {
  $addressForm.slideUp(0);
}

// Smart address form
$(function() {
  const $i18nAddresses = $('.i18n-address');
  $i18nAddresses.each(function () {
    const $form = $(this).closest('form');
    const $countryField = $form.find('select[name=country]');
    const $previewField = $form.find('input.preview');
    $countryField.on('change', () => {
      $previewField.val('on');
      $form.submit();
    });
  });
});

$(document).ready(function() {
  console.log('Hello World');
});
