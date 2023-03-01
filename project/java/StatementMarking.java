package None;

import java.util.List;
import lombok.*;



/* version: 1.1.0 */


/**
  A statement marking is a grouping of characteristics unique to the expression of data MarkingDefinitions (restrictions, permissions, and other guidance for how data can be used and shared) to convey details of a textual marking statement, (e.g., copyright) whose semantic meaning should apply to the associated content. Statement markings are generally not machine-readable. An example of this would be a simple marking to apply copyright information, such as 'Copyright 2014 Acme Inc.'.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class StatementMarking extends MarkingModel {

  private List<String> definitionType;
  private String statement;

}