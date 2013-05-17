### fizzbuzz.rb
### 
### Author:		Graeme Douglas
### Description:	A simple solution to the fizzbuzz problem.  For fun.
### License:		For licensing information, please refer to LICENSE.md
###			in the root of the repository, or contact the author.

def fizzbuzz(n, divisors)
	n.times do |i|
		str = ""
		divisors.each do |e|
			if (i+1) % e[0] == 0
				str << e[1]
			end
		end
		
		if "" == str
			puts i+1
		else
			puts str
		end
	end
end

if __FILE__ == $0
	# Our upper bound.
	n = 30
	# List of replacements.  Don't use hash since order is not guaranteed.
	divisors = [[3, "fizz"], [5, "buzz"]]
	fizzbuzz(n, divisors)
end
