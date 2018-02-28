import '../scss/main.scss';
import 'materialize-css/dist/js/materialize';
import 'jquery.cookie';

/*let csrftoken = $.cookie('csrftoken');

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
);*/

// jQuery Document Ready
$(document).ready(function() {
  console.log('Welcome');
});
