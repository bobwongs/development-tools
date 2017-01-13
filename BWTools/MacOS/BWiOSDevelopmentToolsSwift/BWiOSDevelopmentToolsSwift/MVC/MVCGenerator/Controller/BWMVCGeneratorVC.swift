//
//  BWMVCGeneratorVC.swift
//  BWMacOSStudySwift
//
//  Created by BobWong on 17/1/13.
//  Copyright © 2017年 BobWongStudio. All rights reserved.
//

import Cocoa

class BWMVCGeneratorVC: NSViewController {
    
    // MARK: UI
    @IBOutlet weak var tfModuleName: NSTextField!
    @IBOutlet weak var svProperty: NSScrollView!
    @IBOutlet weak var svGeneration: NSScrollView!
    
    // MARK: View Cycle
    override func viewDidLoad() {
        super.viewDidLoad()
    }
    
    // MARK: Action
    @IBAction func btnActionReset(_ sender: Any) {
        tvMVCSource.string = ""
    }
    
    @IBAction func btnActionGenerate(_ sender: Any) {
        
        // ------------ Set the source ------------
        // ------------ <#Comment#> ------------
        let source = tvMVCSource.string
        let path_source = "\(NSHomeDirectory())/Desktop/Generator/MVC/Source/source.txt"
        let path_generation = "\(NSHomeDirectory())/Desktop/Generator/MVC/Generation/generation.txt"
        
        do {
            // replace all content in source file
            try source?.write(toFile: path_source, atomically: false, encoding: String.Encoding.utf8)
        }
        catch {
            print("MVC Source Write Error!")
        }
        
        // ------------ Execute python script ------------
        guard let path = Bundle.main.path(forResource: "generator_mvc", ofType: "py") else {
            print("no BWStudy.sh path")
            return
        }
        
        let task = Process()
        task.launchPath = "/usr/bin/python"
        task.arguments = [path]
        
        let outputPipe = Pipe()
        task.standardInput = Pipe()
        task.standardOutput = outputPipe
        task.launch()
        task.waitUntilExit()
        
        
        let fileHandle = outputPipe.fileHandleForReading
        let output = NSString.init(data: fileHandle.readDataToEndOfFile(), encoding: String.Encoding.utf8.rawValue)
        print("Output is \(output)")
        
        
        // ------------ Write the result ------------
        do {
            let stringGeneration = try NSString.init(contentsOfFile: path_generation, encoding: String.Encoding.utf8.rawValue)
            tvGeneration.string = stringGeneration as String
        } catch {
            
        }
    }
    
    // MARK: Getter and Setter
    var tvMVCSource: NSTextView {
        get { return svProperty.contentView.documentView as! NSTextView }
    }
    
    var tvGeneration: NSTextView {
        get { return svGeneration.contentView.documentView as! NSTextView }
    }
    
}

/*
 Mac OS Developmemt Study
    // 可以拼接在文件后头
    let fileHandleSource = FileHandle.init(forWritingAtPath: path_source)
    fileHandleSource?.seekToEndOfFile()
    fileHandleSource?.write((source?.data(using: String.Encoding.utf8))!)
    fileHandleSource?.closeFile()
 */
