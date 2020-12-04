require('fs').readFile("./2020/input/day04.txt", "utf8", (err, data) => {
    console.log('part 1:' + [...data.replace(/\r/g, '').matchAll(/(^((byr:[^\s]+)|(iyr:[^\s]+)|(eyr:[^\s]+)|(hgt:[^\s]+)|(hcl:[^\s]+)|(ecl:[^\s]+)|(pid:[^\s]+))( |\n(?!\n))((byr:[^\s]+)|(iyr:[^\s]+)|(eyr:[^\s]+)|(hgt:[^\s]+)|(hcl:[^\s]+)|(ecl:[^\s]+)|(pid:[^\s]+)|( |\n(?!\n))){11})|(^((byr:[^\s]+)|(iyr:[^\s]+)|(eyr:[^\s]+)|(hgt:[^\s]+)|(hcl:[^\s]+)|(ecl:[^\s]+)|(pid:[^\s]+)|(cid:[^\s]+))( |\n(?!\n))((byr:[^\s]+)|(iyr:[^\s]+)|(eyr:[^\s]+)|(hgt:[^\s]+)|(hcl:[^\s]+)|(ecl:[^\s]+)|(pid:[^\s]+)|(cid:[^\s]+)|( |\n(?!\n))){13})/gm)].length)
    console.log('part 2:' + [...data.replace(/\r/g, '').matchAll(/(^((byr:(19[2-8][0-9]|199[0-9]|200[0-2]))|(iyr:(201[0-9]|2020))|(eyr:(202[0-9]|2030))|(hgt:((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in))|(hcl:#[0-9a-f]{6})|(ecl:(amb|blu|brn|gry|grn|hzl|oth))|(pid:\d{9}))( |\n(?!\n))((byr:(19[2-8][0-9]|199[0-9]|200[0-2]))|(iyr:(201[0-9]|2020))|(eyr:(202[0-9]|2030))|(hgt:((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in))|(hcl:#[0-9a-f]{6})|(ecl:(amb|blu|brn|gry|grn|hzl|oth))|(pid:\d{9})|( |\n(?!\n))){11})|(^((byr:(19[2-8][0-9]|199[0-9]|200[0-2]))|(iyr:(201[0-9]|2020))|(eyr:(202[0-9]|2030))|(hgt:((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in))|(hcl:#[0-9a-f]{6})|(ecl:(amb|blu|brn|gry|grn|hzl|oth))|(pid:\d{9})|(cid:[\w\d]+))( |\n(?!\n))((byr:(19[2-8][0-9]|199[0-9]|200[0-2]))|(iyr:(201[0-9]|2020))|(eyr:(202[0-9]|2030))|(hgt:((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in))|(hcl:#[0-9a-f]{6})|(ecl:(amb|blu|brn|gry|grn|hzl|oth))|(pid:\d{9})|(cid:[\w\d]+)|( |\n(?!\n))){13})/gm)].length)
})