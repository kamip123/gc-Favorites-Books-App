	<script src="{% static 'jquery.cookie.js' %}"></script>
      
      <script>
      	var csrftoken = $.cookie('csrftoken');

		function csrfSafeMethod(method) {
		    // these HTTP methods do not require CSRF protection
		    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
		}
		
		$.ajaxSetup({
		    beforeSend: function(xhr, settings) {
		        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		            xhr.setRequestHeader("X-CSRFToken", csrftoken);
		        }
		    }
		});
		
      	$.ajax('https://solwit-pjatk-arc-2018-gr1.appspot.com/profil/allauthorslist', {
		    type: 'POST',
		    data: {
		        imie: 'pepeeeee',
		        nazwisko: 'peopwskiiiiiii',
		        wiek: 34
		    }
		});
      </script>