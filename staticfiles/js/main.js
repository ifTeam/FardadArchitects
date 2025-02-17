let video;

// Video and canvas size factors
let videoHeightFactor = 1 / 4; // Video height is 1/4 of the window height
let canvasHeightFactor = 4; // Canvas height is 4 times the window height

// Grid settings
let gridImages = []; // Array to hold images for the grid
let imagesCount = 6; // Total images in grid
let rowCount = 2; // Number of rows in grid
let colCount = 3; // Number of columns in grid

// Image and layout settings
let imgSize = 250; // Image size (width & height)
let paddingMultiplier = 0.10; // Padding as a percentage of window width
let horizontalGapMultiplier = 0.2; // Horizontal gap as percentage of window width
let verticalGapMultiplier = 0.5; // Vertical gap as percentage of window height

// Computed values
let padding, horizontalGap, verticalGap;

function preload() {
  video = createVideo('/static/videos/logo.mp4'); // Ensure correct path
  video.hide();  

  // Preload images for grid
  for (let i = 0; i < imagesCount; i++) {
    gridImages[i] = loadImage(`/static/images/building${i}.png`); 
  }
}

function setup() {
  computeLayout();
  createCanvas(windowWidth, windowHeight * canvasHeightFactor);  // Set canvas size
  video.size(width, height * videoHeightFactor);  // Set video size
  video.volume(0); // Mute to allow autoplay in some browsers
  video.play();
  video.onended(videoEnded);  // Callback for when video ends
}

function draw() {
  background(255);  
  image(video, 0, 0);  // Always display the video
  drawPhotoGrid();  // Draw image grid
}

function drawPhotoGrid() {
  let gridStartY = height * videoHeightFactor;  // Position grid below video
  
  for (let row = 0; row < rowCount; row++) {  
    for (let col = 0; col < colCount; col++) {  
      let x = padding + col * (imgSize + horizontalGap);  // Calculate x position
      let y = gridStartY + row * (imgSize + verticalGap);  // Calculate y position

      // Draw each image in the grid
      let imgIndex = row * colCount + col;
      if (gridImages[imgIndex]) {
        image(gridImages[imgIndex], x, y, imgSize, imgSize);
      }
    }
  }
}

function computeLayout() {
  padding = windowWidth * paddingMultiplier;
  horizontalGap = windowWidth * horizontalGapMultiplier;
  verticalGap = windowHeight * verticalGapMultiplier;
}

function videoEnded() {
  video.pause();  // Pause the video at the last frame
  video.time(video.duration());  // Set time to last frame
}

function windowResized() {
  resizeCanvas(windowWidth, windowHeight * canvasHeightFactor);
  video.size(width, height * videoHeightFactor);
  computeLayout();  // Recalculate gaps on resize
}
