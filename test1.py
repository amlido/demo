<div class="banner-item" id="banner">
  {% for key, value in content|items %}
  <div class="img__holder" style="background-image: url('{{ image(value.media.src, 600, 1920) }}');">   
    <div class="container">      
          <div class="banner__container">
			  <div class="banner__content">		  
				<h1 class="banner--title">{{value.title}}</h1>
				<h4 class="banner--sub-title">{{value.sub_title|safe}}</h4>
				<p class="banner--desc big">{{value.desc}}</p>
				<a href="#" class="btn btn--md animations btn--no_shadow">{{value.button}}</a>
			  </div>
		</div>
    </div>
  </div>  
  {% endfor %} 
</div>
