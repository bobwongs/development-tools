//
//  BWUIPropertyGeneratorVC.swift
//  BWMacOSStudySwift
//
//  Created by BobWong on 17/1/11.
//  Copyright © 2017年 BobWongStudio. All rights reserved.
//

import Cocoa
import Foundation

class BWUIPropertyGeneratorVC: NSViewController {
    
    // MARK: UI
    @IBOutlet weak var svProperty: NSScrollView!
    @IBOutlet weak var svGeneration: NSScrollView!
    
    // MARK: View Cycle
    override func viewDidLoad() {
        super.viewDidLoad()
    }
    
    // MARK: Action
    @IBAction func btnActionReset(_ sender: AnyObject) {
        tvProperty.string = ""
    }
    @IBAction func btnActionGenerate(_ sender: AnyObject) {
        let task = Process()
        task.launchPath = "/usr/bin/python"
        task.arguments = ["-c", "print \"hello\""]
        
        let outputPipe = Pipe()
        task.standardInput = Pipe()
        task.standardOutput = outputPipe
        task.launch()
        task.waitUntilExit()
        
        
        let fileHandle = outputPipe.fileHandleForReading
        let output = NSString.init(data: fileHandle.readDataToEndOfFile(), encoding: String.Encoding.utf8.rawValue)
        print("Output is \(output)")
    }
    
    
    
    // MARK: Getter and Setter
    var tvProperty: NSTextView {
        get { return svProperty.contentView.documentView as! NSTextView }
    }
    
    var tvGeneration: NSTextView {
        get { return svGeneration.contentView.documentView as! NSTextView }
    }
    
}
