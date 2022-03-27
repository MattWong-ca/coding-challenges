class Assignment {
    
    
    func fibonacci(n: Int) {
    
    var index = 0
    var a = 0
    var b = 1
    var array = [a,b]
    
    while index < n-2 {
        let c = a + b
        array.append(c)
        a = b
        b = c
        
        index += 1
    }
    print(array)
    
    }
}
