// Problem: Come up with possible prime permutation of input integer and return.
// Problem break down: 1) Coming up with permutations
//										 2) Determining prime-or-not
// Hint: To find all possible prime numbers upto 'n', we need to find ones upto sqrt(n)
#include <vector>
#include <iostream>
#include <hashmap
using namespace std;

int main() {
	int input_int = 97263;
	int size = 0;
	int divider = 10;

	while (input_int / divider) {
		size++;
		divider *= 10;
	}

	vector<int> digits(size);
	
	for (int i = 0; i < size; i++) {
		digits[i] = input_int % 10;
		input_int /= 10;
	}
	
	vector<int> prime_perms;
	get_prime_perms(prime_perms, digits, size - 1, size);

	// In order to generate permutations, I need to multiply: digit * 10 ^ size + digit * 10 ^ (size - 1) ... + digit * 10 ^ 0.
	for(int i = 0; i < size; i++) {
		
		perms.pushback();
	}
}

void get_prime_perms(vector<int> prime_perms, vector<int> digits, int size, int digit_place {
	if (size)
		return;
	else {
		for (int i = size; i >= 0; i--) {
			
		}
	}
}

static 
bool check_
