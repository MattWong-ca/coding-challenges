import UIKit
import StoreKit

struct Purchase {
    let productId: String
    let quantity: Int
    let transaction: PaymentTransaction
    let needsFinishTransaction: Bool
}

struct PaymentTransaction {
    var transactionDate: Date?
    var transactionState: SKPaymentTransactionState
    var transactionIdentifier: String?
}

// Question 1
// Look at the documentation for SKPaymentTransactionState
// Create an array of 5 test Purchases, each containing a unique SKPaymentTransactionState

let date = Date()

let paymentTransaction = PaymentTransaction(transactionDate: date, transactionState: .failed, transactionIdentifier: "test" )

let paymentTransaction2 = PaymentTransaction(transactionDate: date, transactionState: .restored, transactionIdentifier: "test1" )

let paymentTransaction3 = PaymentTransaction(transactionDate: date, transactionState: .deferred, transactionIdentifier: "test2" )

let paymentTransaction4 = PaymentTransaction(transactionDate: date, transactionState: .purchased, transactionIdentifier: "test3" )

let paymentTransaction5 = PaymentTransaction(transactionDate: date, transactionState: .purchasing, transactionIdentifier: "test4" )

var purchaseArray = [ Purchase(productId: "test1", quantity: 1, transaction: paymentTransaction, needsFinishTransaction: true), Purchase(productId: "test2", quantity: 2, transaction: paymentTransaction2, needsFinishTransaction: true), Purchase(productId: "test3", quantity: 3, transaction: paymentTransaction3, needsFinishTransaction: true), Purchase(productId: "test4", quantity: 4, transaction: paymentTransaction4, needsFinishTransaction: true), Purchase(productId: "test5", quantity: 5, transaction: paymentTransaction5, needsFinishTransaction: true)]

// Question 2
// Write a method that takes in an array of Purchase objects and returns a list of transactionIdentifiers for which the SKPaymentTransactionState is failed or restored

func failedOrRestored( purchaseArray: [Purchase] ) {
    for object in purchaseArray {
        if object.transaction.transactionState == .failed {
            print("Transaction failed")
        } else if object.transaction.transactionState == .restored {
            print("Transaction restored")
        } else {
            print("Transaction did not fail or restore")
        }
    }
}

failedOrRestored(purchaseArray: purchaseArray)
