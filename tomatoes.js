// Pause the video when the modal is closed
$(document).on('click', '.hanging-close, .modal-backdrop, .modal',
		function(event) {
			// Remove the src so the player itself gets removed, as this is the
			// only reliable way to ensure the video stops playing in IE
			$("#trailer-video-container").empty();
		});

// Start playing the video whenever the trailer modal is opened
$(document).on(
		'click',
		'.view-trailer',
		function(event) {

			var trailerYouTubeId = 'Myv_Z8CReDU';
			var movieId = $(this).attr('data-movie-id')
			var jsonUrl = 'https://api.themoviedb.org/3/movie/' + movieId
					+ '/videos?api_key=23d81fdf84638b37ab9f8d898c12243c';

			// Get YouTube ID from TMDb API (should be moved to webservice)

			$.getJSON(jsonUrl, function(json) {
				$.each(json.results, function(i, video) {
					console.log(video.site + ": " + video.key);
					if (video.site == "YouTube") {
						console.log("Site used is YouTube");
						trailerYouTubeId = video.key;
					}
				});

				var sourceUrl = 'http://www.youtube.com/embed/'
						+ trailerYouTubeId + '?autoplay=1&html5=1';

				$("#trailer-video-container").empty().append(
						$("<iframe></iframe>", {
							'id' : 'trailer-video',
							'type' : 'text-html',
							'src' : sourceUrl,
							'frameborder' : 0
						}));
			});
		});

// Animate in the movie tiles within each row when the page loads
// Commenting out for now, I don't feel this brings a great enough
// effect for the added complexity
//$(document).ready(
//		function() {
//			$('.row').each(
//					function() {
//						$(this).find('#movie-tile').hide().first().show("slow",
//								function showNext() {
//									$(this).next("div").show("slow", showNext);
//								});
//					});
//
//		});
