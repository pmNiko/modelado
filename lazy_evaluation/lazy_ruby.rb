def condicion1
    puts "condición 1 devuelve False"
    return false
end

def condicion2
  puts "condición 2 devuelve True"
  return true
end

puts "\nEvaluación perezosa or lazy evaluation en Ruby\n"

condicion2 && condicion1

puts "\n"

condicion1 && condicion2

puts "\nFin del código en Ruby\n\n"