const getFalse = () => {
  console.log("condición 1 devuelve False");
  return false;
};

const getTrue = () => {
  console.log("condición 2 devuelve true");
  return true;
};

console.log("\nEvaluación perezosa or lazy evaluation en JavaScript\n");

getFalse() && getTrue();

console.log("\n");

getTrue() && getFalse();

console.log("\nFin del código en JavaScript\n");
