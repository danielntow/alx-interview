const myPromise = new Promise((resolve, reject) => {
  // Simulating an asynchronous operation
  setTimeout(() => {
    const randomNumber = Math.random();
    if (randomNumber < 0.5) {
      resolve(randomNumber);
    } else {
      reject(new Error("Random number is greater than or equal to 0.5"));
    }
  }, 1000);
});

myPromise
  .then((result) => {
    console.log("Promise fulfilled with result:", result);
  })
  .catch((error) => {
    console.error("Promise rejected with error:", error);
  });
