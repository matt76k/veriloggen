import noname

expected_verilog = """
module blinkled #
  ( 
   parameter WIDTH = 8
  )
  ( 
   input CLK, 
   input RST,
   output reg [WIDTH-1:0] LED
  );
  reg [32-1:0] _tmp_0;
  reg [32-1:0] _tmp_1;
  wire [32-1:0] _tmp_2;
  reg [32-1:0] _tmp_3;
  wire [32-1:0] _tmp_4;
  reg [32-1:0] _tmp_5;
  wire [32-1:0] _tmp_6;
  always @(posedge CLK) begin
    if(RST) begin
      _tmp_0 <= 0;
    end else begin
      if(_tmp_0 == 1023) begin
        _tmp_0 <= 0;
      end else begin
        _tmp_0 <= _tmp_0 + 1;
      end
    end
  end
  always @(posedge CLK) begin
    if(RST) begin
      LED <= 0;
    end else begin
      if(_tmp_0 == 1023) begin
        LED <= LED + 1;
      end 
    end
  end
endmodule
"""

def test():
    test_module = noname.mkLed()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
