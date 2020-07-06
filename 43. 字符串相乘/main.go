package main

import (
	"strconv"
	"strings"
)

func main() {
}

func multiply(num1 string, num2 string) string {
	if num1 == "0" || num2 == "0" {
		return "0"
	}

	res := "0"
	for i := len(num1) - 1; i >= 0; i-- {
		cur1 := int(num1[i] - '0')
		flag := 0
		buff := make([]string, 0, len(num2)+1+len(num1)-i+1)
		for k := 1; k < len(num1)-i; k++ {
			buff = append(buff, "0")
		}
		for j := len(num2) - 1; j >= 0; j-- {
			cur2 := int(num2[i] - '0')
			mul := cur1*cur2 + flag
			flag = mul / 10
			mulS := strconv.Itoa(mul % 10)
			buff = append(buff, mulS)
		}
		if flag != 0 {
			flagStr := strconv.Itoa(flag)
			buff = append(buff, flagStr)
		}
		res = strAdd(res, Reverse(strings.Join(buff, "")))
	}

	return res

}

func Reverse(s string) string {
	r := []rune(s)
	for i, j := 0, len(r)-1; i < j; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}
	return string(r)
}

func strAdd(num1 string, num2 string) string {
	num1Len, num2Len := len(num1), len(num2)
	var smallLen, bigLen int
	var shortStr, longStr string
	if num1Len < num2Len {
		smallLen = num1Len - 1
		shortStr = num1

		bigLen = num2Len - 1
		longStr = num2
	} else {
		smallLen = num2Len - 1
		shortStr = num2

		bigLen = num1Len - 1
		longStr = num1
	}

	flag := 0
	buff := make([]string, 0, bigLen+1)
	for minPtr, bigPtr := smallLen, bigLen; minPtr >= 0; {
		cur1 := int(shortStr[minPtr] - '0')
		cur2 := int(longStr[bigPtr] - '0')
		sum := cur2 + cur1 + flag
		if sum >= 10 {
			flag = 1
		} else {
			flag = 0
		}
		buff = append(buff, strconv.Itoa(sum%10))
		minPtr--
		bigPtr--
	}
	bigPtr := bigLen - smallLen - 1

	for ; bigPtr >= 0; {
		cur := int(longStr[bigPtr] - '0')
		sum := cur + flag
		if sum >= 10 {
			flag = 1
		} else {
			flag = 0
		}
		bigPtr--
		buff = append(buff, strconv.Itoa(sum%10))
	}

	if flag == 1 {
		buff = append(buff, "1")
	}

	return Reverse(strings.Join(buff, ""))
}
