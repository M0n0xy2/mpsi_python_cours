#include <iostream>
#include <vector>
#include <array>
#include <cstdint>
#include <cmath>

using ulll = uintmax_t;

ulll exp_pow(ulll x, ulll n, ulll mod) {
    ulll answer{ 1 }, remainder;
    while(n) {
        remainder = n % 2;
        n /= 2;
        if(remainder)
            answer = (answer * x) % mod;
        x = ((x % mod) * (x % mod)) % mod;
    }
    return answer;
}

std::vector<ulll> factorise(ulll n) {
    std::vector<ulll> div;
    const auto max = static_cast<ulll>(std::sqrt(n)) + 1;
    for(ulll d{2}; d < max; ++d) {
        while(n % d == 0) {
            n /= d;
            div.push_back(d);
        }
    }
    if(n != 1)
        div.push_back(n);
    return div;
}

bool is_prime(ulll n) {
    static constexpr std::array<ulll, 7> tests{
        {2, 3, 5, 7, 11, 13, 17}
    };
    for(auto t : tests)
        if(exp_pow(t, n-1, n) != 1)
            return false;
    return factorise(n).size() == 1;
}

int main() {
    constexpr ulll start = 10000001;
    constexpr ulll end = 20000000;

    std::vector<ulll> primes;
    primes.reserve((end-start)/4);
    for(auto n = start; n < end; n += 2)
        if(is_prime(n))
            primes.push_back(n);
    std::cout << primes.size() << std::endl;
}
