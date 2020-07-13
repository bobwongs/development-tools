//
//  BWCSSClassGeneratorVC.swift
//  BWiOSDevelopmentToolsSwift
//
//  Created by BobWong on 2018/7/20.
//  Copyright © 2018年 BobWongStudio. All rights reserved.
//

import Cocoa

class BWCSSClassGeneratorVC: NSViewController {

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
    
    @IBAction func btnActionGenerate(_ sender: AnyObject)
    {
        // Set the file path
        let source = tvProperty.string
        let pathDir = "\(NSHomeDirectory())/Desktop/Generator/CSSClassTemplate"
        let pathSource = "\(pathDir)/source.txt"
        let pathGeneration = "\(pathDir)/generation.txt"
        
        // Check file
        if !hasDirectory(path: pathDir) { return }
        if !hasFile(path: pathSource) { return }
        if !hasFile(path: pathGeneration) { }
        
        tvGeneration.string = executePythonScript(scriptInBundle: "generator_css_class", sourcePath: pathSource, generationPath: pathGeneration, source: source, argumentsExceptPath: []) ?? ""
    }
    
    
    
    // MARK: Getter and Setter
    var tvProperty: NSTextView {
        get { return svProperty.contentView.documentView as! NSTextView }
    }
    
    var tvGeneration: NSTextView {
        get { return svGeneration.contentView.documentView as! NSTextView }
    }
    
}
