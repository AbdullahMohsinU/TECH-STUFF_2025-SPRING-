#include "pch.h"
#include "C:\Users\TEMP\Desktop\project\project\mi.cpp"
#include "gtest/gtest.h"

using namespace testing;

using namespace std;
// Define a parameterized test for the add function
class calculatorTest : public TestWithParam<tuple<int, int, int>> {
protected:
	calculator calc; //injstance of calculator
};
TEST_P(calculatorTest, Addition) {
	int a = get<0>(GetParam()); // First input
	int b = get<1>(GetParam()); // Second input
	int result = get<2>(GetParam()); // Expected result
	EXPECT_EQ(calc.addition(a, b), result); // Validate the addition
}
INSTANTIATE_TEST_CASE_P(AdditionT, calculatorTest,Values(
		std::make_tuple(1, 2, 3),
		std::make_tuple(3, 4, 7),
		std::make_tuple(-1, 1, 0),
		std::make_tuple(-5, -6, -11)
	));