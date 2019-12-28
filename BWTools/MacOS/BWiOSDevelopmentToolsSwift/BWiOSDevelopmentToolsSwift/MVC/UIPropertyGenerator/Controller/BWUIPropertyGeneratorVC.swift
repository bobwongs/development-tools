//
//  BWUIPropertyGeneratorVC.swift
//  BWMacOSStudySwift
//
//  Created by BobWong on 17/1/11.
//  Copyright © 2017年 BobWongStudio. All rights reserved.
//

import Cocoa

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
    
    @IBAction func btnActionGenerate(_ sender: AnyObject)
    {
        // Set the file path
        let source = tvProperty.string
        let pathUIPropertyDir = "\(NSHomeDirectory())/Desktop/Generator/UIProperty"
        let pathSource = "\(pathUIPropertyDir)/source.txt"
        let pathGeneration = "\(pathUIPropertyDir)/generation.txt"
        
        // Check file
        if !hasDirectory(path: pathUIPropertyDir) { return }
        if !hasFile(path: pathSource) { return }
        if !hasFile(path: pathGeneration) { }
        
        tvGeneration.string = executePythonScript(scriptInBundle: "generator_property_ui_oc", sourcePath: pathSource, generationPath: pathGeneration, source: source, argumentsExceptPath: []) ?? ""
    }
    
    
    
    // MARK: Getter and Setter
    var tvProperty: NSTextView {
        get { return svProperty.contentView.documentView as! NSTextView }
    }
    
    var tvGeneration: NSTextView {
        get { return svGeneration.contentView.documentView as! NSTextView }
    }
    
}
