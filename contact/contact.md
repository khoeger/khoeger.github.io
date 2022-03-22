## email

[<span class="fa fa-envelope"></span>](mailto:{{site.email}})  &emsp;[katarina[AT]katarinahoeger[DOT]com](mailto:{{site.email}})

<!-- LINK ASSIGNMENT CALCULATIONS -->
{% assign base = 'https://www.linkedin.com/in/'%}
{% assign username = site.linkedin_username %}
{% assign linkedInLink = base | append:  username %}
{% assign base = 'https://twitter.com/'%}
{% assign username = site.twitter_username %}
{% assign twitterLink = base | append:  username %}
{% assign base = 'https://github.com/'%}
{% assign username = site.github_username %}
{% assign githubLink = base | append:  username %}
{% assign base = 'https://soundcloud.com/'%}
{% assign username = site.soundcloud_username %}
{% assign soundcloudLink = base | append:  username %}
{% assign base = 'https://www.instagram.com/'%}
{% assign username = site.instagram_username %}
{% assign instagramLink = base | append:  username %}
## Connect

[<span class="fab fa-github"></span>]({{githubLink}}) &emsp;GitHub [@{{site.github_username}}]({{githubLink}})

[<span class="fab fa-instagram"></span>]({{instagramLink}}) &emsp;Instagram [@{{site.instagram_username}}]({{instagramLink}})

[<span class="fab fa-linkedin"></span>]({{linkedInLink}}) &emsp;LinkedIn [@{{site.linkedin_username}}]({{linkedInLink}})

[<span class="fab fa-soundcloud"></span>]({{soundcloudLink}})&emsp;SoundCloud [@{{site.soundcloud_username}}]({{soundcloudLink}})

[<span class="fab fa-twitter"></span>]({{twitterLink}}) &emsp;Twitter [@{{site.twitter_username}}]({{twitterLink}})



## Subscribe
<!-- https://joelglovier.com/writing/rss-for-jekyll -->
[<span class="fa fa-rss"></span>]({{"/feed.xml" | relative_url }}) &emsp;via [RSS]({{"/feed.xml" | relative_url }})

<!-- https://blog.webjeda.com/jekyll-subscribe-form/#update-1---mailchimp-subscribe-form-on-jekyll -->
[<span class="fa fa-envelope-open"></span>]({{site.mailchimp_signup_link}}) &emsp;via [Mailing List]({{site.mailchimp_signup_link}})
<!-- Begin Mailchimp Signup Form -->
<link href="//cdn-images.mailchimp.com/embedcode/classic-10_7_dtp.css" rel="stylesheet" type="text/css">
<style type="text/css">
	#mc_embed_signup{background:#fff; clear:left; font:14px Helvetica,Arial,sans-serif;  width:300px;}
	/* Add your own Mailchimp form style overrides in your site stylesheet or in this style block.
	   We recommend moving this block and the preceding CSS link to the HEAD of your HTML file. */
</style>
<div id="mc_embed_signup">
<form action="https://katarinahoeger.us14.list-manage.com/subscribe/post?u=e367bc226ccf2d4298cd99b8c&amp;id=4be4d66c52" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="validate" target="_blank" novalidate>
    <div id="mc_embed_signup_scroll">

<div class="indicates-required"><span class="asterisk">*</span> indicates required</div>
<div class="mc-field-group">
	<label for="mce-FNAME">First Name </label>
	<input type="text" value="" name="FNAME" class="" id="mce-FNAME">
</div>
<div class="mc-field-group">
	<label for="mce-LNAME">Last Name </label>
	<input type="text" value="" name="LNAME" class="" id="mce-LNAME">
</div>
<div class="mc-field-group">
	<label for="mce-EMAIL">Email Address  <span class="asterisk">*</span>
</label>
	<input type="email" value="" name="EMAIL" class="required email" id="mce-EMAIL">
</div>
<div hidden="true"><input type="hidden" name="tags" value="7156455"></div>
	<div id="mce-responses" class="clear foot">
		<div class="response" id="mce-error-response" style="display:none"></div>
		<div class="response" id="mce-success-response" style="display:none"></div>
	</div>    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_e367bc226ccf2d4298cd99b8c_4be4d66c52" tabindex="-1" value=""></div>
        <div class="optionalParent">
            <div class="clear foot">
                <input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button">
                <p class="brandingLogo"><a href="http://eepurl.com/hXA-gr" title="Mailchimp - email marketing made easy and fun"><img src="https://eep.io/mc-cdn-images/template_images/branding_logo_text_dark_dtp.svg"></a></p>
            </div>
        </div>
    </div>
</form>
</div>
<script type='text/javascript' src='//s3.amazonaws.com/downloads.mailchimp.com/js/mc-validate.js'></script><script type='text/javascript'>(function($) {window.fnames = new Array(); window.ftypes = new Array();fnames[1]='FNAME';ftypes[1]='text';fnames[2]='LNAME';ftypes[2]='text';fnames[0]='EMAIL';ftypes[0]='email';fnames[3]='ADDRESS';ftypes[3]='address';fnames[4]='PHONE';ftypes[4]='phone';fnames[5]='BIRTHDAY';ftypes[5]='birthday';}(jQuery));var $mcj = jQuery.noConflict(true);</script>
<!--End mc_embed_signup-->
