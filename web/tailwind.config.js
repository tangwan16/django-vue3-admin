/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ['./index.html', './src/**/*.{vue,js}'],
	theme: {
		extend: {
			height:{
				'screen/2': '50vh',
				"righttop":"620px",
			},
			colors: {
			"fontblue":"#19ecff",
			"fontpieinnner":"#7abefc",
			"fonttime":"#31C1FD"
		  	},
			left:{
				"pie":"45px",
			},
		},
	},
	plugins: [],
};
