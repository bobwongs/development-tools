//
//  BWMVCGeneratorVC.swift
//  BWiOSDevelopmentToolsSwift
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
        
        // ------------ Set the path parameters for source and generation directory ------------
        let source = tvMVCSource.string
        let pathMVCDir = "\(NSHomeDirectory())/Desktop/Generator/MVC"
        let pathSourceDir = "\(pathMVCDir)/Source"
        let pathGenerationDir = "\(pathMVCDir)/Generation"
        
        let pathSource = "\(pathSourceDir)/source.txt"
        let pathGeneration = "\(pathGenerationDir)/generation.txt"
        
        // If there not has file, create
        if !hasDirectory(path: pathSourceDir) { return }
        if !hasFile(path: pathSource) { return }
        
        tvGeneration.string = executePythonScript(scriptInBundle: "generator_mvc", sourcePath: pathSource, generationPath: pathGeneration, source: source)
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
    let fileHandleSource = FileHandle.init(forWritingAtPath: pathSource)
    fileHandleSource?.seekToEndOfFile()
    fileHandleSource?.write((source?.data(using: String.Encoding.utf8))!)
    fileHandleSource?.closeFile()
 */
